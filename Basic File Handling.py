def find_and_replace(file_name, word_to_find, word_to_replace):
    try:
        # Read file content
        with open(file_name, "r", encoding="utf-8") as file:
            content = file.read()

        # Perform replacement
        if word_to_find in content:
            updated_content = content.replace(word_to_find, word_to_replace)

            # Save changes back to the file
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(updated_content)

            print(f"✅ All occurrences of '{word_to_find}' have been replaced with '{word_to_replace}'.")
        else:
            print(f"⚠️ The word '{word_to_find}' was not found in the file.")

    except FileNotFoundError:
        print("❌ Error: The file does not exist. Please check the file name.")
    except PermissionError:
        print("❌ Error: You don’t have permission to access this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


def main():
    print("📂 Basic File Handling Program")
    file_name = input("Enter the file name (e.g., data.txt): ").strip()
    word_to_find = input("Enter the word you want to find: ").strip()
    word_to_replace = input("Enter the word you want to replace it with: ").strip()

    find_and_replace(file_name, word_to_find, word_to_replace)


if __name__ == "__main__":
    main()
