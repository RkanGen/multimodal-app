// src/App.js
import React, { useState } from 'react';
import { Container, Typography, Button, MenuItem, Select, FormControl, InputLabel, CircularProgress } from '@mui/material';
import axios from 'axios';

function App() {
  const [selectedModel, setSelectedModel] = useState('');
  const [file, setFile] = useState(null);
  const [result, setResult] = useState('');
  const [loading, setLoading] = useState(false);

  const handleModelChange = (event) => {
    setSelectedModel(event.target.value);
  };

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleUpload = () => {
    if (!file || !selectedModel) {
      alert("Please select a file and a model.");
      return;
    }
    setLoading(true);
    const formData = new FormData();
    formData.append('file', file);
    formData.append('model', selectedModel);

    axios.post('http://localhost:5000/upload', formData)
      .then(response => {
        setResult(response.data.result);
        setLoading(false);
      })
      .catch(error => {
        console.error("There was an error uploading the file!", error);
        setLoading(false);
      });
  };

  return (
    <Container>
      <Typography variant="h4" gutterBottom>
        Multimodal Model Selector
      </Typography>
      <FormControl fullWidth margin="normal">
        <InputLabel>Choose Model</InputLabel>
        <Select value={selectedModel} onChange={handleModelChange}>
          <MenuItem value="stylegan3">StyleGAN3</MenuItem>
          <MenuItem value="sdxl">SDXL</MenuItem>
          <MenuItem value="dall-e">DALL-E</MenuItem>
        </Select>
      </FormControl>
      <input
        accept="image/*,.pdf"
        style={{ display: 'none' }}
        id="raised-button-file"
        type="file"
        onChange={handleFileChange}
      />
      <label htmlFor="raised-button-file">
        <Button variant="contained" component="span" fullWidth>
          Upload File
        </Button>
      </label>
      <Button variant="contained" color="primary" onClick={handleUpload} fullWidth>
        Submit
      </Button>
      {loading && <CircularProgress style={{ marginTop: '20px' }} />}
      {result && (
        <Typography variant="body1" marginTop="20px">
          Result: {result}
        </Typography>
      )}
    </Container>
  );
}

export default App;
