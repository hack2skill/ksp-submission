import React from 'react'

import { Input } from 'antd'
import { EyeInvisibleOutlined, EyeTwoTone } from '@ant-design/icons';
import { HiLockClosed } from 'react-icons/hi'

const Password = ({value,handleState, className}) => {
 
    return (
        <>
            <div className={`font-medium text-lg leading-[1.5rem] capitalize mt-[2.4rem] mb-[4px] ${className}`}>password</div>
            
            <Input.Password size='large'
                placeholder="Enter Password"
                value={value}
                onChange={handleState}
                prefix={<HiLockClosed className='text-lg mr-[0.75rem]' />}
                className=" bg-[#f8f8f8] text-base"
                iconRender={(visible) => (visible ? <EyeTwoTone /> : <EyeInvisibleOutlined />)}
            />
        </>
    )
}

export default Password