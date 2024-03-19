import readFile
import writeFile

websites = (
    'https://wp.pl',
    'https://nike.com',
    'https://wonderfulbrightsplendidmorning.neverssl.com/online/'
)

write_json = writeFile.WriteFile(websites)
readJson = readFile.ReadFile()

write_json.write_json_file()
readJson.read_json_file()
