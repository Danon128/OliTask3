import csv

if __name__ == "__main__":
    alphabetRusCap = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    alphabetRusLower = alphabetRusCap.lower()
    alphabetEng = "abcdefghijklmnopqrstuvwxyz"
    with open("input.csv", encoding="UTF8") as input_csvfile:
        csv_reader = csv.reader(input_csvfile, delimiter=",", lineterminator="\n")
        with open("result.csv", "w", encoding="utf-8") as output_csvfile:
            csv_writer = csv.writer(output_csvfile, delimiter=",", lineterminator="\n")
            for row in csv_reader:
                email, address = row
                last_point = address.rfind(".")
                key = ord(address[last_point - 1]) - ord("в")
                original_email = ""
                for letter in email:
                    if letter in alphabetEng:
                        original_email += alphabetEng[(alphabetEng.find(letter) - key) % len(alphabetEng)]
                    else:
                        original_email += letter
                original_address = ""
                for letter in address:
                    if letter in alphabetRusCap:
                        original_address += alphabetRusCap[(alphabetRusCap.find(letter) - key) % len(alphabetRusCap)]
                    elif letter in alphabetRusLower:
                        original_address += alphabetRusLower[
                            (alphabetRusLower.find(letter) - key) % len(alphabetRusLower)
                        ]
                    else:
                        original_address += letter
                csv_writer.writerow([key, original_email, original_address])
    print("Results are in 'result.csv' file.")
