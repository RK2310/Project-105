import os, cv2

path = "images"
images = []
 
for i in os.listdir(path):
    name, ext = os.path.splitext(i)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+i
        
        images.append(file_name)
        
count = len(images)
frame = cv2.imread(images[0])
height, width, channel = frame.shape
size = (width, height)

out = cv2.VideoWriter("project.avi", cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

for j in range(count-1, 0, -1):
    frame = cv2.imread(images[j])
    out.write(i)
out.release()