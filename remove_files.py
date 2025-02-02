import os

FILE_LIST = "files_to_remove.txt"
REPORT_FILE = "removed_files_report.txt"

# Debug: Print all files in repo
print("\n📂 Checking files in the repository before deletion:")
for root, dirs, files in os.walk("."):
    for file in files:
        print(os.path.join(root, file))

# Read file names from files_to_remove.txt
if not os.path.exists(FILE_LIST):
    print(f"❌ Error: {FILE_LIST} not found.")
    exit(1)

with open(FILE_LIST, "r") as f:
    files_to_remove = f.read().splitlines()

removed_files = []

for file in files_to_remove:
    if os.path.exists(file):
        os.remove(file)
        removed_files.append(file)
        print(f"✅ Removed: {file}")
    else:
        print(f"⚠️ File not found: {file}")

# Generate a report
with open(REPORT_FILE, "w") as report:
    report.write("Removed Files Report\n")
    report.write("====================\n")
    for file in removed_files:
        report.write(f"Removed: {file}\n")

print(f"\n🚀 File removal complete. Report generated: {REPORT_FILE}")
