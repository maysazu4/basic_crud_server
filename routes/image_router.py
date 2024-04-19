from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import StreamingResponse

router = APIRouter()

def load_student_image(student_id):
    # Replace this with your actual logic to load student image from somewhere
    # For example, you might load it from a database or from a file system
    # Here, we'll just load a sample image from a file
    with open(f"student_images/{student_id}.jpg", "rb") as f:
        return f.read()

@router.get("/students/{student_id}/image")
def stream_student_image(student_id: int, request: Request):
    """
    Endpoint to stream the image of a specific student by ID.

    Args:
        student_id (int): The ID of the student whose image to stream.
        request (Request): The HTTP request object.

    Returns:
        StreamingResponse: The streaming response containing the image data.

    Raises:
        HTTPException: If the specified student ID is not found.
    """
    # Load student image data
    image_data = load_student_image(student_id)
    if not image_data:
        raise HTTPException(status_code=404, detail="Student image not found")

    # Create a generator to yield image data in chunks
    def image_generator():
        yield image_data

    # Set response headers for image content
    headers = {
        "Content-Type": "image/jpeg",  # Adjust content type according to your image format
    }

    # Return streaming response
    return StreamingResponse(image_generator(), headers=headers)