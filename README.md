### **Launch Instructions:**
1. Build an image from a Dockerfile: `docker build -t wine_quality_image .`
2. Derive a container from the image: `docker run -e MODEL_NAME='model_name.pkl' -p host_port:container_port wine_quality_image`
3. Make curl to check: `curl -d input_json http://localhost:host_port/predict`

