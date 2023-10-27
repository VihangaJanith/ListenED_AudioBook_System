import './App.css';
import Navbar from './components/Navbar/NavBar';
import { Route, BrowserRouter as Router, Routes } from 'react-router-dom'
import AudioBooksPage from './pages/AudioBooksPage';

function App() {
  return (
    <div>
      <Router>
        <Navbar />
        <Routes>
          <Route path="/" element={<AudioBooksPage />} />
        </Routes>

      </Router>
    </div>
  );
}

export default App;
