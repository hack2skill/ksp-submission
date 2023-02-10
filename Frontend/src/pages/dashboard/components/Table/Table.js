import React from "react";
import {
  Table,
  TableRow,
  TableHead,
  TableBody,
  TableCell,
} from "@material-ui/core";

export default function TableComponent({ data }) {

  return (
    <Table className="mb-0">
      <TableHead>
        <TableRow>
          <TableCell className="pl-3 fw-normal">Name</TableCell>
          <TableCell>Person Name</TableCell>
          <TableCell>Father Name</TableCell>
          <TableCell>Permanent Address</TableCell>
          <TableCell>District Name</TableCell>
          <TableCell>State</TableCell>
          <TableCell>Gender</TableCell>
          <TableCell>Age</TableCell>
        </TableRow>
      </TableHead>
      <TableBody>
        {data.map(({ _id, _source }) => (
          <TableRow key={_id}>
            <TableCell className="pl-3 fw-normal">{_source.Name}</TableCell>
            <TableCell>{_source.Person_Name}</TableCell>
            <TableCell>{_source.Father_Name}</TableCell>
            <TableCell>{_source.Perm_Address1}</TableCell>
            <TableCell>{_source.District_Name}</TableCell>
            <TableCell>{_source.State}</TableCell>
            <TableCell>{_source.Gender}</TableCell>
            <TableCell>{_source.Age}</TableCell>
            {/* <TableCell>
              <Chip label={status} classes={{root: classes[states[status.toLowerCase()]]}}/>
            </TableCell> */}
          </TableRow>
        ))}
      </TableBody>
    </Table>
  );
}
