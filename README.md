# React + Vite +Fast APi

The frontend  interact 
with this FastAPI backend to:
upload files, 
select models, and display the results.
This setup provides a complete end-to-end solution for handling multimodal model :<br>
+++++++++++++++++++++++++++++++++++++++++++++++++++++++<br>
RUN this in Bash<br>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++<br>
Front-end<br>
npx create-react-app multimodal-app <br>
cd multimodal-app<br>
npm install @mui/material @emotion/react @emotion/styled axios<br>
npm start<br>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Back-end<br>
pip install fastapi uvicorn<br>
uvicorn app:app --reload<br>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 The purpose of this project;<br>
the integration of StyleGAN3, SDXL, and DALL-E models into your FastAPI backend. The backend handles file uploads, processes them with the selected model, and returns the processed results to the frontend. Adjust the processing functions according to the actual inference code of the models you are using.
