import { SearchIcon } from '@chakra-ui/icons';
import {
  Box,
  Button,
  Center,
  HStack,
  Input,
  InputGroup,
  InputLeftElement,
  Link,
  Text,
  useColorModeValue,
  useDisclosure,
} from '@chakra-ui/react';
import { useState } from 'react';
import BottomSearch from '../components/BottomSearch';
import PhoneSearch from '../components/PhoneSearch';

const Links = ['Dashboard', 'Projects', 'Team'];

const NavLink = () => (
  <Link
    px={2}
    py={1}
    rounded={'md'}
    _hover={{
      textDecoration: 'none',
      bg: useColorModeValue('gray.200', 'gray.700'),
    }}
    href={'#'}
  >
    hi
  </Link>
);

export default function Dashboard() {
  const { isOpen, onOpen, onClose } = useDisclosure();
  const [textType, setTextType] = useState(null);
  const [isSearched, setSearch] = useState(false);

  return (
    <>
      <Box px={24} py="18">
        <Center>
          <Text px="2" py="8" fontWeight={'bold'} fontSize="lg">
            Search for publicly available information
          </Text>
        </Center>
        <HStack>
          <InputGroup>
            <InputLeftElement
              p="2"
              pointerEvents="none"
              children={<SearchIcon color="gray.300" />}
            />
            <Input type="tel" placeholder="Enter search information" />
          </InputGroup>
          <Button
            colorScheme="green"
            w="10%"
            m="2"
            onClick={() => setSearch(true)}
          >
            Search
          </Button>
        </HStack>
        <Text pl="5" pt="5" color={'gray.500'} fontSize="xs">
          Search for phone number +91 (xxxxx) <br></br>Search for email
          (abc@xyz.com) <br /> Search for userid - instagram, facebook, userid
          @(abc)
        </Text>
        {isSearched ? (
          <Box mt="10">
            {/* facebook */}
            <PhoneSearch />
          </Box>
        ) : (
          <BottomSearch />
        )}
      </Box>
    </>
  );
}
