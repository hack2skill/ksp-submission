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
import axios from 'axios';
import {
  Accordion,
  AccordionButton,
  AccordionIcon,
  AccordionItem,
  AccordionPanel,
} from '@chakra-ui/react';

import { Table, Tbody, Td, Th, Thead, Tr } from '@chakra-ui/react';
import { useEffect } from 'react';
import UpiInfo from '../components/UpiInfo';

const telegramdata = {
  peer: { userId: '894241062', className: 'PeerUser' },
  chats: [],
  users: [
    {
      flags: 33554511,
      self: false,
      contact: false,
      mutualContact: false,
      deleted: false,
      bot: false,
      botChatHistory: false,
      botNochats: false,
      verified: false,
      restricted: false,
      min: false,
      botInlineGeo: false,
      support: false,
      scam: false,
      applyMinPhoto: true,
      fake: false,
      botAttachMenu: false,
      premium: false,
      attachMenuEnabled: false,
      flags2: 0,
      id: '894241062',
      accessHash: '-8230826335575738556',
      firstName: 'Suraj',
      lastName: 'Kumar',
      username: 'psk907',
      phone: null,
      photo: null,
      status: { className: 'UserStatusRecently' },
      botInfoVersion: null,
      restrictionReason: null,
      botInlinePlaceholder: null,
      langCode: null,
      emojiStatus: null,
      usernames: null,
      className: 'User',
    },
  ],
  className: 'contacts.ResolvedPeer',
};

export default function Dashboard() {
  const { isOpen, onOpen, onClose } = useDisclosure();
  // const [textType, setTextType] = useState(null);
  const [isSearched, setSearch] = useState(false);
  const [searchstring, setss] = useState('');

  const [truecallerdata, getTruecaller] = useState();
  const [newtruecaller, setnew] = useState({});
  const [iswhats, setwhats] = useState();

  const truecallerarraylist = [
    'phones',
    'addresses',
    'internetAddresses',
    'badges',
    'tags',
    'sources',
    'searchWarnings',
  ];

  function getTelegram(searchString) {
    axios
      .get(
        'https://00a7-119-161-98-68.in.ngrok.io/telegram?phno=' + searchString
      )
      .then(a => {
        getTruecaller(a?.data);
        console.log(a?.data);

        setnew({
          id: truecallerdata?.data[0]?.id,
          access: truecallerdata?.data[0]?.access,
          phones: truecallerdata?.data[0]?.phones,
          addresses: truecallerdata?.data[0]?.addresses,
          internetAddresses: truecallerdata?.data[0]?.internetAddresses,
          badges: truecallerdata?.data[0]?.addresses,
          tags: truecallerdata?.data[0]?.tags,
          sources: truecallerdata?.data[0]?.sources,
          searchWarnings: truecallerdata?.data[0]?.searchWarnings,
        });
      });
  }

  function getTruecallerDatafun(searchString) {
    axios
      .get(
        'https://00a7-119-161-98-68.in.ngrok.io/truecaller?phno=' + searchString
      )
      .then(a => {
        getTruecaller(a?.data);
        console.log(a?.data);

        setnew({
          id: truecallerdata?.data[0]?.id,
          access: truecallerdata?.data[0]?.access,
          phones: truecallerdata?.data[0]?.phones,
          addresses: truecallerdata?.data[0]?.addresses,
          internetAddresses: truecallerdata?.data[0]?.internetAddresses,
          badges: truecallerdata?.data[0]?.addresses,
          tags: truecallerdata?.data[0]?.tags,
          sources: truecallerdata?.data[0]?.sources,
          searchWarnings: truecallerdata?.data[0]?.searchWarnings,
        });
      });
  }

  useEffect(() => {
    console.log(newtruecaller);
    console.log('vfnviefnv');
  }, [newtruecaller]);

  return (
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
          <Input
            type="tel"
            placeholder="Enter search information"
            onChange={e => {
              setss(e.target.value);
              console.log(e.target.value);
            }}
          />
        </InputGroup>
        <Button
          colorScheme="green"
          w="10%"
          m="2"
          onClick={e => {
            setSearch(true);
            getTruecallerDatafun(searchstring);
          }}
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
          <>
            <Box px={8}>
              <Text>Phone Search</Text>
              <Accordion defaultIndex={[]} allowMultiple>
                <AccordionItem bg={'#EDF2F7'}>
                  <h2>
                    <AccordionButton>
                      <Box as="span" flex="1" textAlign="left">
                        <Text fontWeight={'bold'}>Whatsapp Account</Text>
                      </Box>
                      <AccordionIcon />
                    </AccordionButton>
                  </h2>
                  <AccordionPanel pb={4}>
                    To check if this number has a whatsapp account please click
                    the below link
                    <br />
                    <Link
                      href={'https://wa.me/+91' + searchstring}
                      target="_blank"
                    >
                      https://wa.me/+91{searchstring}
                    </Link>
                  </AccordionPanel>
                </AccordionItem>

                <AccordionItem>
                  <h2>
                    <AccordionButton>
                      <Box as="span" flex="1" textAlign="left">
                        <Text fontWeight={'bold'}>Telegram Account</Text>
                        <Text>found</Text>
                      </Box>
                      <AccordionIcon />
                    </AccordionButton>
                  </h2>
                  <AccordionPanel pb={4}>
                    <Table
                      whiteSpace={'normal'}
                      variant="simple"
                      size="s"
                      mb="34"
                      w={'100%'}
                    >
                      <Thead>
                        <Tr>
                          <Th>Dataset</Th>
                          <Th>Information Available</Th>
                        </Tr>
                      </Thead>
                      <Tbody>
                        {Object.keys(telegramdata.users[0]).map(e => {
                          if (
                            e == 'firstName' ||
                            e == 'lastName' ||
                            e == 'username'
                          )
                            return (
                              <Tr>
                                <Td>{e}</Td>
                                <Td>
                                  <Box w="100" fontWeight={'bold'} color="red">
                                    {telegramdata?.users[0][e]?.toString()}
                                  </Box>
                                </Td>
                              </Tr>
                            );
                          else {
                            return (
                              <Tr>
                                <Td>{e}</Td>
                                <Td>
                                  <Box w="100">
                                    {telegramdata?.users[0][e]?.toString()}
                                  </Box>
                                </Td>
                              </Tr>
                            );
                          }
                        })}
                      </Tbody>
                    </Table>
                  </AccordionPanel>
                </AccordionItem>
                <AccordionItem bg={'#EDF2F7'}>
                  <h2>
                    <AccordionButton>
                      <Box as="span" flex="1" textAlign="left">
                        <Text fontWeight={'bold'}>Truecaller Account</Text>
                        <Text>found</Text>
                      </Box>
                      <AccordionIcon />
                    </AccordionButton>
                  </h2>
                  <AccordionPanel pb={4}>
                    <Table
                      whiteSpace={'normal'}
                      variant="simple"
                      size="s"
                      mb="34"
                      w={'100%'}
                    >
                      <Thead>
                        <Tr>
                          <Th>Dataset</Th>
                          <Th>Information Available</Th>
                        </Tr>
                      </Thead>
                      <Tbody>
                        {newtruecaller.id != undefined &&
                          Object.keys(newtruecaller).map(e => {
                            console.log('-----------');
                            // console.log(newtruecaller);
                            console.log(e);
                            if (truecallerarraylist.includes(e))
                              return (
                                <Tr>
                                  <Td>{e}</Td>
                                  {newtruecaller[e].map(newe => {
                                    return (
                                      <Td>
                                        <Table size="s">
                                          {Object.keys(newe).map(i => {
                                            return (
                                              <Tr>
                                                <Td>{i}</Td>
                                                <Td>{newe[i]}</Td>
                                              </Tr>
                                            );
                                          })}
                                        </Table>
                                        <Box w="100">
                                          {newtruecaller[e].toString()}
                                        </Box>
                                      </Td>
                                    );
                                  })}
                                </Tr>
                              );
                            else
                              return (
                                <Tr>
                                  <Td>{e}</Td>
                                  <Td>
                                    <Box w="100">
                                      {newtruecaller[e].toString()}
                                    </Box>
                                  </Td>
                                </Tr>
                              );
                          })}
                      </Tbody>
                    </Table>
                  </AccordionPanel>
                </AccordionItem>
              </Accordion>

              <Box my="10">
                <UpiInfo input={searchstring} type="phone" />
              </Box>
            </Box>
          </>
        </Box>
      ) : (
        <BottomSearch />
      )}
    </Box>
  );
}
