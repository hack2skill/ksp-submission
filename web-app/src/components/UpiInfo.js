import { Box, Card, List, ListItem, OrderedList } from '@chakra-ui/react';

export default function UpiInfo({ input, type = 'email' }) {
  const phone = ['paytm', 'ybl', 'axl', 'ibl'];
  const email = ['okicici', 'okaxis', 'okhdfcbank', 'oksbi'];
  return (
    <>
      <Box>You can check the following for the existing UPI ids</Box>

      <OrderedList>
        {type == 'phone' &&
          phone.map(e => {
            return <ListItem>{input + '@' + e}</ListItem>;
          })}
      </OrderedList>

      <OrderedList>
        {type == 'email' &&
          email.map(e => {
            return <ListItem>{input + '@' + e}</ListItem>;
          })}
      </OrderedList>
    </>
  );
}
