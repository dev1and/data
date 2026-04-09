"""
YAMLエントリーの重複をチェックするツール

概要:
  team.yaml などの YAML ファイル内のエントリーが重複していないかチェックします。
  RSSのURL（正規化後）、サイトのURL、または名前の類似性に基づいて判定し、
  重複が見つかった場合はそれぞれの行番号を表示します。
  ※このツールはファイルの書き換えを行わず、報告のみを行います。

使い方:
  python3 tools/check_target_deduplicate.py <YAMLファイルパス>

例:
  python3 tools/check_target_deduplicate.py target/ja/tech/team.yaml
"""

import re
import os
import sys

def normalize_rss(rss):
    if not rss: return ""
    rss = rss.strip().lower()
    # プロトコルとサブドメインの除去
    rss = re.sub(r'^https?://(www\.)?', '', rss)
    # 末尾のスラッシュ除去
    rss = rss.rstrip('/')
    # 一般的なサフィックスの除去
    suffixes = [
        '/rss', '/feed', '/index.xml', '/atom.xml', '/rss.xml', 
        '/rss2', '/rdf', '/index.rdf', '/atom', '/feed/atom',
        '.rss', '.xml'
    ]
    for suffix in suffixes:
        if rss.endswith(suffix):
            rss = rss[:-len(suffix)]
            break
    return rss.rstrip('/')

def normalize_url(url):
    if not url: return ""
    url = url.strip().lower()
    url = re.sub(r'^https?://(www\.)?', '', url)
    return url.rstrip('/')

def normalize_name(name):
    if not name: return ""
    # スペース、記号を除去して英数字のみにする
    return re.sub(r'[^a-zA-Z0-9]', '', name).lower()

def parse_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    entries = []
    current = None

    for i, line in enumerate(lines):
        line_num = i + 1
        if line.startswith("- name:"):
            if current:
                entries.append(current)
            current = {
                'name': line.replace("- name:", "", 1).strip().strip('"').strip("'"),
                'line': line_num,
                'fields': {}
            }
        elif current is not None:
            if ':' in line:
                key, val = line.split(':', 1)
                key = key.strip()
                val = val.strip().strip('"').strip("'")
                current['fields'][key] = val

    if current:
        entries.append(current)
    return entries

def check_duplicates(entries):
    rss_map = {}
    url_map = {}
    name_map = {}

    found_duplicates = False

    for entry in entries:
        fields = entry['fields']
        rss = normalize_rss(fields.get('rss', ''))
        url = normalize_url(fields.get('url', ''))
        name = normalize_name(entry['name'])

        duplicate_of = None

        # 1. RSS によるチェック
        if rss and rss in rss_map:
            duplicate_of = rss_map[rss]
            reason = f"RSS match ({rss})"
        # 2. URL によるチェック
        elif url and url in url_map:
            duplicate_of = url_map[url]
            reason = f"URL match ({url})"
        # 3. 名前によるチェック
        elif name and name in name_map:
            duplicate_of = name_map[name]
            reason = f"Name match ({name})"

        if duplicate_of is not None:
            if not found_duplicates:
                print("Duplicates detected:")
                found_duplicates = True

            print(f"- '{entry['name']}' (Line {entry['line']})")
            print(f"    is duplicate of '{duplicate_of['name']}' (Line {duplicate_of['line']})")
            print(f"    Reason: {reason}")
            continue

        # ユニークなエントリーとして登録（最初に見つかったものを基準にする）
        if rss: rss_map[rss] = entry
        if url: url_map[url] = entry
        if name: name_map[name] = entry

    if not found_duplicates:
        print("No duplicates found.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 tools/check_target_deduplicate.py <filename>")
        sys.exit(1)

    target = sys.argv[1]
    if not os.path.exists(target):
        print(f"Error: {target} not found")
        sys.exit(1)

    entries = parse_yaml(target)
    print(f"Checking {len(entries)} entries in {target}...\n")

    check_duplicates(entries)
