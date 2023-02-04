import { CloseIcon, HamburgerIcon, SearchIcon } from '@chakra-ui/icons';
import {
  Avatar,
  Box,
  Button,
  Card,
  CardBody,
  CardHeader,
  Center,
  chakra,
  Flex,
  Grid,
  Heading,
  HStack,
  IconButton,
  Input,
  InputGroup,
  InputLeftElement,
  Link,
  Menu,
  MenuButton,
  MenuDivider,
  MenuItem,
  MenuList,
  shouldForwardProp,
  Stack,
  Text,
  useColorModeValue,
  useDisclosure,
} from '@chakra-ui/react';
import { isValidMotionProp, motion } from 'framer-motion';
import { useState } from 'react';
import police from '../assets/police.png';
import profile from '../assets/profile.webp';
import ChakraaBox from '../components/chakrabox';
import ChakraBox from '../components/chakrabox';

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

  return (
    <>
      <Box
        bg={useColorModeValue('gray.100', 'gray.900')}
        // UNCOMMENT
        // bgGradient="linear(to-l,#002499, #04123d )"
        px={4}
      >
        <Flex h={20} alignItems={'center'} justifyContent={'space-between'}>
          <IconButton
            size={'md'}
            icon={isOpen ? <CloseIcon /> : <HamburgerIcon />}
            aria-label={'Open Menu'}
            display={{ md: 'none' }}
            onClick={isOpen ? onClose : onOpen}
          />
          <HStack spacing={8} alignItems={'center'}>
            <Box>
              <Avatar src={police} alt="KSP" />
            </Box>

            <Text fontSize="xl" fontWeight={'bold'} color="white">
              KSP Crowdsourcing Dashboard
            </Text>
          </HStack>
          <Flex alignItems={'center'}>
            <Menu>
              <MenuButton
                as={Button}
                rounded={'full'}
                variant={'link'}
                cursor={'pointer'}
                minW={0}
              >
                <Avatar size={'sm'} src={profile} />
              </MenuButton>
              <MenuList>
                <MenuItem>Profile</MenuItem>
                <MenuItem>History</MenuItem>
                <MenuDivider />
                <MenuItem>Logout</MenuItem>
              </MenuList>
            </Menu>
          </Flex>
        </Flex>

        {isOpen ? (
          <Box pb={4} display={{ md: 'none' }}>
            <Stack as={'nav'} spacing={4}>
              {Links.map(link => (
                <NavLink key={link}>{link}</NavLink>
              ))}
            </Stack>
          </Box>
        ) : null}
      </Box>

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
          <Button colorScheme="green" w="10%" m="2">
            Search
          </Button>
        </HStack>
        <Text pl="5" pt="5" color={'gray.500'} fontSize="xs">
          Search for phone number +91 (xxxxx) <br></br>Search for email
          (abc@xyz.com) <br /> Search for userid - instagram, facebook, userid
          @(abc)
        </Text>

        <Box pt="10">
          <Center>
            <Grid templateColumns="repeat(3, 1fr)" gap={6}>
              <Card
                variant={'outline'}
                _hover={{
                  bg: 'teal.300',
                  // transform: transform(1.5),
                  color: 'white',
                  // }}
                }}
              >
                <CardHeader>
                  <Heading size="md">hi</Heading>
                </CardHeader>
                <CardBody>
                  <Text>variant = hi</Text>
                </CardBody>
              </Card>

              <Card
                variant={'outline'}
                _hover={{
                  bg: 'teal.300',
                  color: 'white',
                  // }}
                }}
              >
                <CardHeader>
                  <Heading size="md">hi</Heading>
                </CardHeader>
                <CardBody>
                  <Text>variant = hi</Text>
                </CardBody>
              </Card>
            </Grid>
          </Center>
        </Box>
      </Box>
    </>
  );
}
