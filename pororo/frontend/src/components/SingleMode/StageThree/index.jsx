import { useNavigate } from 'react-router-dom';
import './index.css';

const StageThree = () => {
  const navigate = useNavigate(); // 페이지 이동을 위한 React Router 훅

  return (
    <div className="stage-three-container">
      <button className="home-button" onClick={() => navigate('/single')}>
      ↩
      </button>
      <h1>이야기 나누기</h1>
      <p>은선언니의 네모의 꿈 너무 기대된다</p>
      <p>정우야 너는 알루미늄 준비해와</p>
      <p>다음 회식을 기대해주세요 ~~ </p>
    </div>
  );
};

export default StageThree;
