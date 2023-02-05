import React, {useState} from "react";
import {Checkbox, FormControl, InputLabel, ListItemIcon, ListItemText, MenuItem, Select} from "@mui/material";
import {makeStyles} from "@mui/styles";
const MultiSelectDrop=({labelled_name,options})=>{
    const [selected, setSelected] = useState(options);

    const useStyles = makeStyles((theme) => ({
        formControl: {
            margin: theme.spacing(1),
            width: 300
        },
        indeterminateColor: {
            color: "#f50057"
        },
        selectAllText: {
            fontWeight: 500
        },
        selectedAll: {
            backgroundColor: "rgba(0, 0, 0, 0.08)",
            "&:hover": {
                backgroundColor: "rgba(0, 0, 0, 0.08)"
            }
        }
    }));
    const classes = useStyles();
    const handleChange = (event) => {
        const value = event.target.value;
        if (value[value.length - 1] === "all") {
            setSelected(selected.length === options.length ? [] : options);
            return;
        }
        setSelected(value);
    };
    const ITEM_HEIGHT = 48;
    const ITEM_PADDING_TOP = 8;
    const MenuProps = {
        PaperProps: {
            style: {
                maxHeight: ITEM_HEIGHT * 4.5 + ITEM_PADDING_TOP,
                width: 250
            }
        },
        getContentAnchorEl: null,
        anchorOrigin: {
            vertical: "bottom",
            horizontal: "center"
        },
        transformOrigin: {
            vertical: "top",
            horizontal: "center"
        },
        variant: "menu"
    };
    const isAllSelected =
        options.length > 0 && selected.length === options.length;
    return <FormControl variant="filled" sx={{ m: 1, maxWidth: 300 }} size={"small"}>
        <InputLabel id="mutiple-select-label">{labelled_name}</InputLabel>
        <Select
            labelId="mutiple-select-label"
            multiple
            value={selected}
            onChange={handleChange}
            renderValue={(selected) => selected.join(", ")}
            MenuProps={MenuProps}
            style={{
                border:"none"
            }}
        >
            <MenuItem
                value="all"
                classes={{
                    root: isAllSelected ? classes.selectedAll : ""
                }}
            >
                <ListItemIcon>
                    <Checkbox
                        classes={{ indeterminate: classes.indeterminateColor }}
                        checked={isAllSelected}
                        indeterminate={
                            selected.length > 0 && selected.length < options.length
                        }
                    />
                </ListItemIcon>
                <ListItemText
                    classes={{ primary: classes.selectAllText }}
                    primary="Select All"
                />
            </MenuItem>
            {options.map((option) => (
                <MenuItem key={option} value={option}>
                    <ListItemIcon>
                        <Checkbox checked={selected.indexOf(option) > -1} />
                    </ListItemIcon>
                    <ListItemText primary={option} />
                </MenuItem>
            ))}
        </Select>
    </FormControl>
}
export default MultiSelectDrop;
