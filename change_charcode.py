import codecs
# import io
# import csv

src_file_path = "test.log"
src_codec = codecs.lookup("shift_jis")

dest_file_path = "test_utf8.log"
dest_codec = codecs.lookup("utf_8")


with codecs.open(src_file_path, "r", "shift_jis") as fsrc, codecs.open(dest_file_path, "w", "utf-8") as fdest:
    for row in fsrc:
        fdest.write(row)

# this code is not work.
# with open(src_file_path, "rb") as src, open(dest_file_path, "wb") as dest:
#     # 変換ストリームを作成
#     stream = codecs.StreamRecoder(
#         stream=src,
#         encode=dest_codec.encode,
#         decode=src_codec.decode,
#         Reader=src_codec.streamreader,
#         Writer=dest_codec.streamwriter,
#         errors='strict'
#     )
#     reader = io.BufferedReader(stream)

#     # 書き込み
#     while True:
#         data = reader.read1()
#         if not data:
#             break
#         dest.write(data)
#         dest.flush()


# with open('utf8.csv', 'w', newline='', encoding='utf8') as f:
#     writer = csv.writer(f)
#     writer.writerow(['商品名', '価格'])
#     writer.writerow(['りんご', '300'])
#     writer.writerow(['みかん', '200'])
#     writer.writerow(['パイナップル', '500'])
# with open('utf8.csv', encoding='utf8') as f_in:
#     with open('shiftjis.csv', 'w', encoding='shift_jis') as f_out:
#         f_out.write(f_in.read())
