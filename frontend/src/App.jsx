import { useState, useEffect } from 'react'
import ContactList from './ContactList'
import ContactForm from './ContactForm'
import './App.css'


function App() {
  //Setting our contacts into a state to use
  const [contacts, setContacts] = useState([])

  //creating the Modal
  const [isModalOpen, setIsModalOpen] = useState(false)

  const [currentContact, setCurrentContact] = useState({})

  //To perform the fetchContacts function and display contacts to the internface as soon as the site loads up 
  //When the page loads ups, perform the function and it will end up displaying our data to the console
  useEffect(() => { 
    fetchContacts() 
  }, [])



  //fetching the contacts, but wll wait until 
      //Response will fetch our api endpoint site (get)
      //data will extract our json from our end point - {"contacts" : []}
      //data.contacts give us just the list of contacts [] since we are calling it using the dictionarys key
      //We load these contacts into our setContact state
      //We output the data to the frotnend interface using console.log
  const fetchContacts = async () => {
    const response = await fetch("http://127.0.0.1:5000/contacts")
    const data = await response.json()  
    setContacts(data.contacts)
    //console.log(data.contacts) 
  }



  // functions to run modal
  const closeModal = () => {
    setIsModalOpen(false)
    setCurrentContact({})
  }

  //if modal is not open then open the modal
  const openCreateModal = () => {
    if (!isModalOpen) setIsModalOpen(true)
  }


  const openEditModal = (contact) => {
    if (isModalOpen) return
    setCurrentContact(contact)
    setIsModalOpen(true)
  }



  const onUpdate = () => {
    closeModal()
    fetchContacts()
  }




  //Redner the contacts list and display
  //to also display the modal
  return (
    <>
      < ContactList contacts = {contacts} updateContact = {openEditModal} updateCallback = {onUpdate}  />
      <button onClick = {openCreateModal}>Create New Contact</button>
      {isModalOpen && <div className = "modal">
        <div className = "modal-content">
          <span className = "close" onClick = {closeModal}>&times;</span>
          < ContactForm existingContact = {currentContact} updateCallback = {onUpdate} />
        </div>
      </div>
      }
    </>

  )
    
}

export default App;
