"""
YAMLエントリーを名前順にソートするツール

概要:
  team.yaml などの YAML ファイル内のエントリーを name フィールドの値に基づいて
  アルファベット順（ケースインセンシティブ）にソートします。
  ファイルのヘッダー部分は維持されます。

使い方:
  python3 tools/sort_target_by_name.py <YAMLファイルパス>

例:
  python3 tools/sort_target_by_name.py target/ja/tech/team.yaml
"""

import sys
import os

def sort_yaml(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # エントリーごとに分割
    entries = []
    current_entry = []
    lines = content.splitlines()

    header = []
    found_first_entry = False

    for line in lines:
        # エントリーの開始を検出
        if line.startswith("- name:"):
            found_first_entry = True
            if current_entry:
                entries.append("\n".join(current_entry))
            current_entry = [line]
        else:
            if not found_first_entry:
                header.append(line)
            else:
                current_entry.append(line)

    if current_entry:
        entries.append("\n".join(current_entry))

    # nameフィールドの値（小文字）でソート
    def get_sort_key(entry):
        for line in entry.splitlines():
            if line.startswith("- name:"):
                # "- name: " の部分を除去してトリム
                name = line.replace("- name:", "", 1).strip().strip('"').strip("'")
                return name.lower()
        return ""

    entries.sort(key=get_sort_key)

    # コンテンツの再構築
    result = []
    if header:
        result.append("\n".join(header))
    result.extend(entries)

    final_content = "\n".join(result)
    if not final_content.endswith("\n"):
        final_content += "\n"

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(final_content)

    print(f"Successfully sorted {len(entries)} entries in {file_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 tools/sort_target_by_name.py <filename>")
    else:
        # 指定されたファイルパスをソート実行
        target_file = sys.argv[1]
        sort_yaml(target_file)
