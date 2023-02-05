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

export default function BottomSearch() {
  return (
    <Box pt="20">
      <Center>
        <Grid templateColumns="repeat(3, 1fr)" gap={6}>
          <LinkBox as="article" maxW="sm" p="3" borderWidth="1px" rounded="md">
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

          <LinkBox as="article" maxW="sm" p="3" borderWidth="1px" rounded="md">
            <Center mb="2" fontStyle={'semibold'}>
              Location Monitoring
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
                <LinkOverlay href="/location-services" target="_blank">
                  View social activity at the target location
                </LinkOverlay>
              </Heading>
              <Text>Query by Latitude or Longitude</Text>
            </Card>
          </LinkBox>
        </Grid>
      </Center>
    </Box>
  );
}
