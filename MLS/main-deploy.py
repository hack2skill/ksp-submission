from fastapi import FastAPI

app =FastAPI()

@app.get("/image_process")
def process_image():
    # # Get the binary data from the request body    
    # image_data = request.data 
    # # Open the binary data as an image    
    # image = Image.open(BytesIO(image_data))
    # # Save the image to a file on local  
    
    print("helloworld")
    
    return "Image saved successfully."
