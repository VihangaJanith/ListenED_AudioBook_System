import React from 'react'

import Navbar from './components/Navbar/NavBar'
import Predict from './pages/Predict'
import Profile from './pages/Profile'
import AudioPlayer from './pages/AudioPlayer'
import AudioBooksPage from './pages/AudioBooksPage'
import Recommendations from './pages/Recommendations'

import { Route, BrowserRouter as Router, Routes } from 'react-router-dom'

function App() {


  return (
    <div>
      <Router>
        <Navbar />
        <Routes>

          <Route path="/" element={<Predict />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="/:id" element={<AudioPlayer />} />
          <Route path="/books-home" element={<AudioBooksPage />} />
          <Route path="/recommendations" element={<Recommendations />} />

        </Routes>

      </Router>
    </div>
  )
}

export default App