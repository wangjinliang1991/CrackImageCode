from aip import AipOcr
# python SDK

APP_ID: '14408430'
API_KEY: 'FrkXesqdodXNpmFxgltdp7Ch'
SECRET_KEY: 'ul4iU4pZW19a4WTnFf8Lq7TBOXpI975X '


client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(file):
    with open(file, 'rb') as fp:
        return fp.read()

image = get_file_content('code.jpg')
"""调用通用物体识别"""
result = client.basicGeneral(image)
print(result)


# def img_to_str(image_path):
#     image = get_file_content(image_path)
#     result = client.basicGenera(image_path)
#     if 'words_result' in result:
#         return '\n'.join([w['words'] for w in result['words_result']])
#
# if __name__ == "__main__":
#     print(img_to_str('code.jpg'))
