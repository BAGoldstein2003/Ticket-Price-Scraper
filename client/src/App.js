import './App.css';
import Input from './components/Input.js';
import Navbar from './components/Navbar.js';
import Loading from './components/Loading.js'
import {useState} from 'react';
import {motion} from 'framer-motion'
import {BrowserRouter, Routes, Route} from 'react-router-dom'



function App() {
  const [isLoading, setIsLoading] = useState(false);


  return (
    <BrowserRouter>
      <motion.div
       initial={{opacity: 0}}
       animate={{opacity: 1}}
       exit={{opacity: 0}}>
        {
        isLoading && <Loading></Loading>
        }
      </motion.div>
      
      <div className={`App ${isLoading && 'loading'}`}>
        <Navbar className='navbar'/>
        <h1>Welcome to Ticket-Price Scraper!</h1>
        <Input className='input' setIsLoading={setIsLoading}/>
        
      </div>
      <Routes>
        <Route path='/scrape' element={<Scrape></Scrape>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;