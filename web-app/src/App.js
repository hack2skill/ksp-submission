import React from 'react';
import {
  ChakraProvider,
  Box,
  Text,
  Link,
  VStack,
  Code,
  Grid,
  theme,
} from '@chakra-ui/react';
import { ColorModeSwitcher } from './ColorModeSwitcher';
import { Logo } from './Logo';
import Dashboard from './screens/Dashboard';

function App() {
  return (
    <ChakraProvider theme={theme}>
      <Dashboard />
    </ChakraProvider>
  );
}

export default App;
