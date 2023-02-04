import { SearchIcon } from '@chakra-ui/icons';
import {
  Box,
  Button,
  Card,
  CardBody,
  CardHeader,
  Center,
  Grid,
  Heading,
  HStack,
  Input,
  InputGroup,
  InputLeftElement,
  Link,
  LinkBox,
  LinkOverlay,
  Text,
  useColorModeValue,
  useDisclosure,
} from '@chakra-ui/react';
import { useState } from 'react';

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
              <LinkBox
                as="article"
                maxW="sm"
                p="3"
                borderWidth="1px"
                rounded="md"
              >
                <Center mb="2" fontStyle={'semibold'}>
                  Additional - Email
                </Center>
                <Card
                  p="4"
                  variant={'outline'}
                  _hover={{
                    bg: 'teal.300',
                    // transform: transform(1.5),
                    color: 'white',
                    // }}
                  }}
                >
                  <Heading size="md" my="2">
                    <LinkOverlay href="/pawned" target="_blank">
                      Check if the email has been pawned
                    </LinkOverlay>
                  </Heading>
                  <Text>
                    This also allows you to find their activity on other sites
                  </Text>
                </Card>
              </LinkBox>

              <LinkBox
                as="article"
                maxW="sm"
                p="5"
                borderWidth="1px"
                rounded="md"
              >
                <LinkOverlay href="#">hi</LinkOverlay>
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
                {/* </LinkOverlay> */}
              </LinkBox>

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
