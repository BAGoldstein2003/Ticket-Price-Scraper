import './Input.css'
import {useState} from 'react'

export default function Input({setIsLoading}) {
    const [formData, setFormData] = useState({ 'url': '', 'threshold': ''})

    const handleURLChange = (e) => {
        setFormData((prevData) => ({
            ...prevData,
            'url': e.target.value
        }));
    }

    const handleThresholdChange = (e) => {
        if (!isNaN(e.target.value)) {
            setFormData((prevData) => ({
                ...prevData,
                'threshold': e.target.value
            }))
        }
    }

    const handleSubmit = async () => {
        console.log('submitted:')
        console.log(formData)
        setIsLoading(true)
        setTimeout(() => {
            setIsLoading(false)
        }, 1000)
    }

    return (
        <div className='input'>
            <h1>Enter Your TickPick Event URL:</h1>
            <input className='url' name='url' onChange={handleURLChange} value={formData.url} ></input>
            <h1>Then Enter a Dollar Amount Threshold:</h1>
            <input className='threshold' name='threshold' onChange={handleThresholdChange} value={formData.threshold}></input>
            <button className='submit' onClick={handleSubmit}>Scrape</button>
        </div>
    )
}