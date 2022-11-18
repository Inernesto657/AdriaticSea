import Login from "./components/login";
import Dashboard from "./components/dashboard";
import Preferences from "./components/preferences";
import Questions from "./components/questions";
import Newslist from "./components/newslist";
import {BrowserRouter as Router,Route,Routes} from "react-router-dom";

function App() {
  return (  
    <div> 
     <Router>
    <Routes>
      <Route path="/login" element={<Login/>} exact/>
      <Route path="/dashboard" element={<Dashboard/>} exact/>
      <Route path="/preferences" element={<Preferences/>} exact/>
      <Route path="/questions" element={<Questions/>} exact/>
      <Route path="/newslist" element={<Newslist/>} exact/>
    </Routes>
    </Router>
    </div>
  );
}

export default App;
