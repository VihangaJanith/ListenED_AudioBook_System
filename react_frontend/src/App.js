import React from 'react'
import Predict from './Predict'

import { Route, BrowserRouter as Router, Routes } from 'react-router-dom'
import Profile from './Profile'
import Navbar from './NavBar'
import AudioPlayer from './AudioPlayer'
import AudioBooksPage from './AudioBooksPage'
import Recommendations from './Recommendations'

function App() {


  return (
    <div>
      <Navbar />
      <Router>

        <Routes>

          <Route path="/" element={<AudioBooksPage />} />

          <Route path="/profile" element={<Profile />} />
          <Route path="/:id" element={<AudioPlayer />} />
          <Route path="/books-home" element={<AudioBooksPage />} />
          <Route path="/recommendations" element={<Recommendations />} />
        </Routes>

      </Router>


      {/* <Predict/> */}
    </div>
  )
}

export default App