import { Box, Divider, LinkOverlay, Text } from '@chakra-ui/react';
import {
  Table,
  Thead,
  Tbody,
  Tfoot,
  Tr,
  Th,
  Td,
  TableCaption,
  TableContainer,
} from '@chakra-ui/react';
import { Link } from '@chakra-ui/react';

const data = [
  {
    Name: 'bigbasket',
    Title: 'bigbasket',
    Domain: 'bigbasket.com',
    BreachDate: '2020-10-14',
    AddedDate: '2021-04-26T04:00:10Z',
    ModifiedDate: '2021-04-26T06:15:01Z',
    PwnCount: 24500011,
    Description:
      'In October 2020, the Indian grocery platform <a href="https://indianexpress.com/article/business/business-others/bigbasket-data-breach-user-details-leaked-dark-web-cyber-crime-7009578/" target="_blank" rel="noopener">bigbasket suffered a data breach that exposed over 20 million customer records</a>. The data was originally sold before being leaked publicly in April the following year and included email, IP and physical addresses, names, phones numbers, dates of birth passwords stored as Django(SHA-1) hashes.',
    LogoPath:
      'https://haveibeenpwned.com/Content/Images/PwnedLogos/bigbasket.png',
    DataClasses: [
      'Dates of birth',
      'Email addresses',
      'IP addresses',
      'Names',
      'Passwords',
      'Phone numbers',
      'Physical addresses',
    ],
    IsVerified: true,
    IsFabricated: false,
    IsSensitive: false,
    IsRetired: false,
    IsSpamList: false,
    IsMalware: false,
  },

  {
    Name: 'Canva',
    Title: 'Canva',
    Domain: 'canva.com',
    BreachDate: '2019-05-24',
    AddedDate: '2019-08-09T14:24:01Z',
    ModifiedDate: '2019-08-09T14:24:01Z',
    PwnCount: 137272116,
    Description:
      'In May 2019, the graphic design tool website <a href="https://support.canva.com/contact/customer-support/may-24-security-incident-faqs/" target="_blank" rel="noopener">Canva suffered a data breach</a> that impacted 137 million subscribers. The exposed data included email addresses, usernames, names, cities of residence and passwords stored as bcrypt hashes for users not using social logins. The data was provided to HIBP by a source who requested it be attributed to "JimScott.Sec@protonmail.com".',
    LogoPath: 'https://haveibeenpwned.com/Content/Images/PwnedLogos/Canva.png',
    DataClasses: [
      'Email addresses',
      'Geographic locations',
      'Names',
      'Passwords',
      'Usernames',
    ],
    IsVerified: true,
    IsFabricated: false,
    IsSensitive: false,
    IsRetired: false,
    IsSpamList: false,
    IsMalware: false,
  },

  {
    Name: 'Canva',
    Title: 'Canva',
    Domain: 'canva.com',
    BreachDate: '2019-05-24',
    AddedDate: '2019-08-09T14:24:01Z',
    ModifiedDate: '2019-08-09T14:24:01Z',
    PwnCount: 137272116,
    Description:
      'In May 2019, the graphic design tool website <a href="https://support.canva.com/contact/customer-support/may-24-security-incident-faqs/" target="_blank" rel="noopener">Canva suffered a data breach</a> that impacted 137 million subscribers. The exposed data included email addresses, usernames, names, cities of residence and passwords stored as bcrypt hashes for users not using social logins. The data was provided to HIBP by a source who requested it be attributed to "JimScott.Sec@protonmail.com".',
    LogoPath: 'https://haveibeenpwned.com/Content/Images/PwnedLogos/Canva.png',
    DataClasses: [
      'Email addresses',
      'Geographic locations',
      'Names',
      'Passwords',
      'Usernames',
    ],
    IsVerified: true,
    IsFabricated: false,
    IsSensitive: false,
    IsRetired: false,
    IsSpamList: false,
    IsMalware: false,
  },
];

export default function Pawned() {
  return (
    <Box m={'8'} spacing="2">
      <Text>Information fetched from hvrvoerv for the email/phone</Text>
      <TableContainer mt="6" p="8" fontSize={'xs'}>
        {data.map(dataitem => {
          return (
            <>
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
                  {Object.keys(dataitem).map(e => {
                    if (e == 'Domain' || e == 'LogoPath') {
                      return (
                        <Tr>
                          <Td>{e}</Td>
                          <Td>
                            <Link href={dataitem[e]} target="_blank">
                              <Text as="u" fontWeight={'semibold'} color="blue">
                                {dataitem[e]}
                              </Text>
                            </Link>
                          </Td>
                        </Tr>
                      );
                    } else if (dataitem[e] == true || dataitem[e] == false) {
                      return (
                        <Tr>
                          <Td>{e}</Td>
                          <Td>{dataitem[e].toString()}</Td>
                        </Tr>
                      );
                    } else if (e == 'DataClasses') {
                      return (
                        <Tr>
                          <Td>{e}</Td>
                          <Td>
                            <Text fontWeight={'semibold'}>
                              {dataitem[e].join(' | ')}
                            </Text>
                          </Td>
                        </Tr>
                      );
                    } else {
                      return (
                        <Tr>
                          <Td>{e}</Td>
                          <Td>
                            <Box w="100">{dataitem[e]}</Box>
                          </Td>
                        </Tr>
                      );
                    }
                  })}
                </Tbody>
              </Table>
            </>
          );
        })}
      </TableContainer>
    </Box>
  );
}
