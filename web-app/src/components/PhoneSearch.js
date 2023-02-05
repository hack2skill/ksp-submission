import axios from 'axios';
import {
  Accordion,
  AccordionButton,
  AccordionIcon,
  AccordionItem,
  AccordionPanel,
  Box,
  Tag,
  TagLabel,
  Text,
} from '@chakra-ui/react';

import { Table, Tbody, Td, Th, Thead, Tr } from '@chakra-ui/react';
import { useState, useEffect } from 'react';
import UpiInfo from './UpiInfo';
export default function PhoneSearch({ searchString }) {
  const initialTrueCaller = {
    data: [
      {
        id: 'XwzLH77u3MaOJFgX+u+fvQ==',
        access: 'PUBLIC',
        enhanced: true,
        phones: [
          {
            e164Format: '+91990280046',
            numberType: 'UNKNOWN',
            nationalFormat: '990280046',
            dialingCode: 91,
            countryCode: 'IN',
            carrier: '',
            type: 'openPhone',
          },
        ],
        addresses: [{ countryCode: 'IN', type: 'address' }],
        internetAddresses: [],
        badges: [],
        tags: [],
        cacheTtl: 86400000,
        sources: [],
        searchWarnings: [],
        surveys: [
          {
            id: '100',
            frequency: 3600,
            passthroughData: 'eyAiMyI6ICI5MTk5MDI4MDA0NiIgfQ==',
            perNumberCooldown: 7890000,
          },
          {
            id: 'b6588ff4-47cb-46ce-8b11-015199c1f729',
            frequency: 3600,
            passthroughData: 'eyAiMyI6ICI5MTk5MDI4MDA0NiIgfQ==',
            perNumberCooldown: 7890000,
          },
        ],
        commentsStats: { showComments: false },
        ns: 100,
      },
    ],
    provider: 'ss-nu',
    stats: { sourceStats: [] },
  };
  const [newtruecaller, settrucallerdata] = useState({});

  const truecallerarraylist = [
    'phones',
    'addresses',
    'internetAddresses',
    'badges',
    'tags',
    'sources',
    'searchWarnings',
  ];

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
  useEffect(() => {
    console.log(searchString + ' ccdcosmcksj');

    axios
      .get(
        'https://00a7-119-161-98-68.in.ngrok.io/truecaller?phno=' + searchString
      )
      .then(a =>
        settrucallerdata({
          id: a?.data?.data[0]?.id,
          access: a?.data?.data[0]?.access,
          phones: a?.data?.data[0]?.phones,
          addresses: a?.data?.data[0]?.addresses,
          internetAddresses: a?.data?.data[0]?.internetAddresses,
          badges: a?.data?.data[0]?.addresses,
          tags: a?.data?.data[0]?.tags,
          sources: a?.data?.data[0]?.sources,
          searchWarnings: a?.data?.data[0]?.searchWarnings,
        })
      );
    console.log(newtruecaller);
  }, [searchString]);

  const chip = (
    <Tag size={'sm'} borderRadius="full" variant="solid" colorScheme="green">
      <TagLabel>FOUND</TagLabel>
    </Tag>
  );

  return (
    <>
      <Box px={8}>
        <Text>Phone Search</Text>
        <Accordion defaultIndex={[]} allowMultiple>
          <AccordionItem bg={'#EDF2F7'}>
            <h2>
              <AccordionButton>
                <Box as="span" flex="1" textAlign="left">
                  <Text fontWeight={'bold'}>Whatsapp Account</Text>
                  {chip}
                </Box>
                <AccordionIcon />
              </AccordionButton>
            </h2>
            <AccordionPanel pb={4}>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
              eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
              enim ad minim veniam, quis nostrud exercitation ullamco laboris
              nisi ut aliquip ex ea commodo consequat.
            </AccordionPanel>
          </AccordionItem>

          <AccordionItem>
            <h2>
              <AccordionButton>
                <Box as="span" flex="1" textAlign="left">
                  <Text fontWeight={'bold'}>Telegram Account</Text>
                  {chip}
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
                    if (e == 'firstName' || e == 'lastName' || e == 'username')
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
                  <Text fontWeight={'bold'}>Telegram Account</Text>
                  {chip}
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
                  {Object.keys(newtruecaller).map(e => {
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
                                <Box w="100">{newtruecaller[e].toString()}</Box>
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
                            <Box w="100">{newtruecaller[e].toString()}</Box>
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
          <UpiInfo input="xxx" type="phone" />
        </Box>
      </Box>
    </>
  );
}
