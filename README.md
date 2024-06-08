# React + Vite +Fast APi

The frontend  interact 
with this FastAPI backend to:
upload files, 
select models, and display the results.
This setup provides a complete end-to-end solution for handling multimodal model :
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
RUN this in Bash
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Front-end
npx create-react-app multimodal-app
cd multimodal-app
npm install @mui/material @emotion/react @emotion/styled axios
npm start
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Back-end
pip install fastapi uvicorn
uvicorn app:app --reload
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 The purpose of this project;
the integration of StyleGAN3, SDXL, and DALL-E models into your FastAPI backend. The backend handles file uploads, processes them with the selected model, and returns the processed results to the frontend. Adjust the processing functions according to the actual inference code of the models you are using.
