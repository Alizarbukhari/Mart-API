# import { useState, useEffect} from 'react';
# import axios from 'axios';

# const Users = ()=> {
#     const [users, setUsers] = useState([]);
#     const [username, setUsername] = useState('');
#     const [email, setEmail] = useState('');

#     useEffect(() => {
#         axios.get('http://localhost:8010/users/')
#             .then(response => setUsers(response.data))
#             .catch(error => console.error('There was an error fetching the users!', error));
#     }, []);

#     const addUser = () => {
#         const newUser = { id: users.length + 1, username, email };
#         axios.post('http://localhost:8010/users/', newUser)
#             .then(response => setUsers([...users, response.data]))
#             .catch(error => console.error('There was an error adding the user!', error));
#     };

#     const deleteUser = (id) => {
#         axios.delete(`http://localhost:8010/users/${id}`)
#             .then(() => setUsers(users.filter(user => user.id !== id)))
#             .catch(error => console.error('There was an error deleting the user!', error));
#     };

#     return (
#         <div>
#             <h1>User Management</h1>
#             <input
#                 type="text"
#                 placeholder="Username"
#                 value={username}
#                 onChange={(e) => setUsername(e.target.value)}
#             />
#             <input
#                 type="email"
#                 placeholder="Email"
#                 value={email}
#                 onChange={(e) => setEmail(e.target.value)}
#             />
#             <button onClick={addUser}>Add User</button>
#             <ul>
#                 {users.map(user => (
#                     <li key={user.id}>
#                         {user.username} - {user.email}
#                         <button onClick={() => deleteUser(user.id)}>Delete</button>
#                     </li>
#                 ))}
#             </ul>
#         </div>
#     );
# };

# export default Users;
