const express = require('express');
const axios = require('axios');
const cors = require('cors');

const app = express();
const PORT = 8080;

app.use(cors());
app.use(express.json());

const FASTAPI_URL = 'http://127.0.0.1:8000';

app.get('/tools', async (req, res) => {
    try {
        const response = await axios.get(`${FASTAPI_URL}/tools`);
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

app.post('/add-tool', async (req, res) => {
    try {
        const response = await axios.post(`${FASTAPI_URL}/add-tool`, req.body);
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

app.get('/tools/:name', async (req, res) => {
    try {
        const response = await axios.get(`${FASTAPI_URL}/tools/${req.params.name}`);
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

app.post('/update-tool', async (req, res) => {
    try {
        const response = await axios.post(`${FASTAPI_URL}/update-tool`, req.body);
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});


