import os

# print(os.listdir('emails/uploads'))
dirListing = os.listdir('emails/uploads')
for item in dirListing:
    # os.path.join(os.getcwd(), "emails/uploads", item)
    os.rename(os.path.join(os.getcwd(), "emails/uploads", item),
              os.path.join(os.getcwd(), "emails/old", item))
