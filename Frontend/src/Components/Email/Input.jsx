import React from 'react'

import { Input } from 'antd';

const Inputfield = ({prefix,type,placeholder,label,value,handleState, className, classNameInput}) => {
    return (
        <>
            <div className={`font-medium text-lg leading-[1.5rem] capitalize mt-[2.4rem] mb-[4px] ${className}`}>{label}</div>

            <Input type={type} 
            value={value} 
            placeholder={placeholder} 
            onChange={handleState}
            prefix={<div className='text-xl mr-[0.75rem]'>{prefix}</div>} 
            size="large" 
            className={`bg-[#f8f8f8] ${classNameInput}`} 
            />
            
        </>
    )
}

export default Inputfield