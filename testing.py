import os


class uploadDocs:
    def __init__(self, pic, text):
        self.pic = ''
        self.text = ''


imageEnding = ('.png', '.jpg', '.jpeg')

# p1 = uploadDocs("", "")
dirListing = os.listdir('emails/uploads')
print(dirListing)
for item in dirListing:
    if item.endswith(imageEnding):
        uploadDocs.pic = item
    elif item.endswith('.txt'):
        uploadDocs.text = item
    os.path.join(os.getcwd(), "emails/uploads", item)
    os.rename(os.path.join(os.getcwd(), "emails/uploads", item),
              os.path.join(os.getcwd(), "emails/old", item))

print(os.path.join(os.getcwd(), uploadDocs.pic))
print(os.path.join(os.getcwd(), uploadDocs.text))