import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';
import Login from './components/User/Login';
import Signup from './components/User/Signup';
import FindId from './components/User/FindId';
import FindPw from './components/User/FindPw';
import MainPage from './components/MainPage';
import SingleMode from './components/SingleMode';
import StageOne from './components/SingleMode/StageOne';
import StageTwo from './components/SingleMode/StageTwo';
import StageThree from './components/SingleMode/StageThree';
import MultiMode from './components/MultiMode';
function App() {
  return (
    <Router>
      <div className="container">
        <Routes>
          <Route path="/" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/find-id" element={<FindId />} />
          <Route path="/find-pw" element={<FindPw />} />
          <Route path="/main" element={<MainPage />} />
          <Route path="/single" element={<SingleMode />} />
          <Route path="/stage-one" element={<StageOne />} />
          <Route path="/stage-two" element={<StageTwo />} />
          <Route path="/stage-three" element={<StageThree />} />
          <Route path="/multi" element={<MultiMode />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
