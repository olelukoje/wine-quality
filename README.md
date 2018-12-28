#### **Launch Instructions:**
1. Build an image from a Dockerfile: docker build -t wine_quality_image .
2. Derive a container from the image: docker run -p host_port:container_port wine_quality_image
3. Make curl to check: curl -d ./wine_inputs.json http://localhost:host_port/predict

