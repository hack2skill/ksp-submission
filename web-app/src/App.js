import { ChakraProvider, theme } from '@chakra-ui/react';
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import NavBar from './components/NavBar';
import Dashboard from './screens/Dashboard';
import Pawned from './screens/Pawned';

function App() {
  return (
    <ChakraProvider theme={theme}>
      <NavBar />
      <Router>
        <Routes>
          <Route exact path="/" element={<Dashboard />} />
          <Route exact path="/pawned" element={<Pawned />} />
        </Routes>
      </Router>
    </ChakraProvider>
  );
}

export default App;
