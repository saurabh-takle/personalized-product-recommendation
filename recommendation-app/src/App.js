import React, { useState, useEffect } from "react";
import axios from "axios";
import {
  CircularProgress,
  Button,
  TextField,
  Typography,
  Container,
  Switch,
  AppBar,
  Toolbar,
  IconButton,
  slotProps,
} from "@mui/material";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import { Brightness4, Brightness7 } from "@mui/icons-material";

function App() {
  const [userId, setUserId] = useState("");
  const [recommendations, setRecommendations] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [darkMode, setDarkMode] = useState(false);

  const theme = createTheme({
    palette: {
      mode: darkMode ? "dark" : "light",
      primary: {
        main: darkMode ? "#90caf9" : "#1976d2", // Light Blue in dark mode, Default Blue in light mode
      },
      secondary: {
        main: darkMode ? "#f48fb1" : "#d32f2f", // Pink in dark mode, Red in light mode
      },
      background: {
        default: darkMode ? "#000" : "#fff", // Dark Gray in Dark Mode, Light Gray in Light Mode
      },
    },
  });

  useEffect(() => {
    document.body.className = darkMode ? "dark-mode" : "light-mode";
  }, [darkMode]);

  const getRecommendations = async () => {
    if (!userId) {
      setError("Please enter a valid User ID.");
      return;
    }
    setLoading(true);
    setError("");
    try {
      const response = await axios.get(
        `https://personalized-product-recommendation.onrender.com/recommend?user_id=${userId}`
      );
      setRecommendations(response.data.recommendations || []);
      setError("");
    } catch (error) {
      console.error("Error fetching recommendations:", error);
      setError("Failed to fetch recommendations. Please try again.");
    }
    setLoading(false);
  };

  return (
    <ThemeProvider theme={theme}>
      <Container
        style={{ textAlign: "center", marginTop: "50px" }}
        sx={{
          backgroundColor: theme.palette.background.default,
          color: darkMode ? "#ffffff" : "#000000",
        }}
      >
        <AppBar
          position="static"
          sx={{
            backgroundColor: darkMode ? "#90caf9" : "#1976d2",
            color: darkMode ? "#000" : "#fff",
          }}
        >
          <Toolbar>
            <Typography variant="h6" style={{ flexGrow: 1 }}>
              Product Recommendation System
            </Typography>
            <IconButton color="inherit" onClick={() => setDarkMode(!darkMode)}>
              {darkMode ? <Brightness7 /> : <Brightness4 />}
            </IconButton>
            <Switch
              sx={{
                color: darkMode ? "#fff" : "#fff",
              }}
              checked={darkMode}
              onChange={() => setDarkMode(!darkMode)}
            />
          </Toolbar>
        </AppBar>

        <TextField
          label="Enter User ID"
          variant="outlined"
          type="number"
          value={userId}
          onChange={(e) => setUserId(e.target.value)}
          style={{ marginBottom: "20px", marginTop: "20px" }}
          slotProps={{
            inputLabel: {
              style: { color: darkMode ? "#90caf9" : "#1976d2" }, // Change label color
            },
          }}
          sx={{
            "& .MuiOutlinedInput-root": {
              "& fieldset": {
                borderColor: darkMode ? "#90caf9" : "#1976d2", // Change border color
              },
              "&:hover fieldset": {
                borderColor: darkMode ? "#f48fb1" : "#d32f2f", // Hover effect
              },
            },
          }}
        />

        <br />

        <Button
          variant="contained"
          color="primary"
          onClick={getRecommendations}
          style={{
            marginBottom: "20px",
          }}
        >
          Get Recommendations
        </Button>

        {loading && <CircularProgress color="primary" />}

        {error && <Typography color="error">{error}</Typography>}

        <Typography variant="h6">Recommended Products:</Typography>
        <ul style={{ listStyleType: "none", padding: 0 }}>
          {recommendations.length > 0
            ? recommendations.map((product, index) => (
                <li key={index} style={{ fontSize: "18px", marginTop: "5px" }}>
                  {product}
                </li>
              ))
            : !loading && <Typography>No recommendations found.</Typography>}
        </ul>
      </Container>
    </ThemeProvider>
  );
}

export default App;
