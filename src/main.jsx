import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import './index.css';

function MyApp() {
  const [theme, setTheme] = React.useState('light');

  const toggleTheme = () => {
    setTheme(theme === 'light' ? 'dark' : 'light');
  };

  return (
    <React.StrictMode>
      <div>
        <button onClick={toggleTheme}>Toggle Theme</button>
        <div
          style={{
            backgroundColor: theme === 'light' ? '#f9f9f9' : '#333',
            padding: 20,
            borderRadius: 10,
            width: 200,
            height: 200,
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
          }}
        >
          <App />
        </div>
      </div>
    </React.StrictMode>
  );
}

ReactDOM.render(<MyApp />, document.getElementById('root'));