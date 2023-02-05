import {
  Box,
  Divider,
  HStack,
  Image,
  Button,
  Input,
  LinkOverlay,
  Text,
  Center,
  Grid,
  GridItem,
  AspectRatio,
} from '@chakra-ui/react';
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
import axios from 'axios';
import { useState } from 'react';

export default function LocationServices() {
  const [lat, setLat] = useState();
  const [long, setLong] = useState();
  const [snapData, setSnapData] = useState(null);

  const updateLat = e => {
    e.preventDefault();
    setLat(e.target.value);
  };

  const updateLong = e => {
    e.preventDefault();
    setLong(e.target.value);
  };

  const searchLatLong = _ => {
    axios
      .get('http://localhost:5001/snapsAtLocation?lat=' + lat + '&long=' + long)
      .then(r => {
        if (r.data['elements'].length == 0) return;
        setSnapData(r.data['elements']);
        console.log(r.data['elements']);
      })
      .catch(e => console.log(e));
  };
  return (
    <Box m={'8'} spacing="2">
      <Text fontWeight={'bold'} color="black">
        Find social media activity by location
      </Text>
      <Box my={8}>
        <HStack justifyContent={'space-around'}>
          <Box>
            <Text>Latitude</Text>
            <Input onChange={updateLat}></Input>
          </Box>
          <Box>
            <Text>Longitude</Text>
            <Input onChange={updateLong}></Input>
          </Box>
        </HStack>
        <Center>
          <Button onClick={searchLatLong}>Search</Button>
        </Center>
      </Box>
      <Grid templateColumns="repeat(5, 1fr)" gap={6}>
        {snapData &&
          snapData.map(a =>
            a.snapInfo.snapMediaType == 'SNAP_MEDIA_TYPE_VIDEO' ? (
              <AspectRatio ratio={0.5}>
                <iframe
                  src={a.snapInfo.streamingMediaInfo.mediaUrl}
                  allowFullScreen
                />
              </AspectRatio>
            ) : (
              <GridItem pr={'2rem'}>
                <Image src={a.snapInfo.streamingMediaInfo.mediaUrl} />
              </GridItem>
            )
          )}
      </Grid>
    </Box>
  );
}
