import { useNavigate } from 'react-router-dom';
import './index.css';

const FindId = () => {
  const navigate = useNavigate(); // 페이지 이동을 위한 React Router 훅

  const handleSubmit = (e) => {
    e.preventDefault();
    alert('아이디 찾기 요청이 완료되었습니다.');
    navigate('/'); // 요청 후 로그인 페이지로 이동
  };

  return (
    <div className="form-container">
      <h2>아이디 찾기</h2>
      <form onSubmit={handleSubmit}>
        <div className="input-group">
          <input
            className="input"
            type="email"
            id="email"
            name="email"
            placeholder="이메일"
            required
          />
        </div>
        <button className="button" type="submit">
          아이디 찾기
        </button>
      </form>
      <button className="secondary-button" onClick={() => navigate('/')}>
        로그인으로 돌아가기
      </button>
    </div>
  );
};

export default FindId;
