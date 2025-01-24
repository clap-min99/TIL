import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import api from './api'; // Axios 인스턴스 가져오기
import './index.css'; // 기존 CSS 유지

const Signup = () => {
  const [formData, setFormData] = useState({
    user_id: '', // 로그인 ID
    password: '', // 비밀번호
    email: '', // 이메일
    name: '', // 자녀 이름
  });

  const navigate = useNavigate(); // 페이지 이동을 위한 React Router 훅

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    // 필드 유효성 검사
    if (!formData.user_id || !formData.password || !formData.email || !formData.name) {
      alert('모든 필드를 입력해주세요.');
      return;
    }

    // 서버로 데이터 전송
    api
      .post('/api/signup', formData)
      .then((response) => {
        // 성공 시
        alert(response.data.message || '회원가입이 완료되었습니다!');
        navigate('/'); // 로그인 화면으로 이동
      })
      .catch((error) => {
        // 실패 시
        console.error('Error during signup:', error);
        if (error.response) {
          alert(error.response.data.message || '회원가입에 실패했습니다.');
        } else {
          alert('서버와 연결할 수 없습니다.');
        }
      });
  };

  return (
    <div className="form-container">
      <h2>회원가입</h2>
      <form onSubmit={handleSubmit}>
        <div className="input-group">
          <input
            className="input"
            type="text"
            id="user_id"
            name="user_id"
            placeholder="로그인 ID"
            value={formData.user_id}
            onChange={handleChange}
            required
          />
        </div>
        <div className="input-group">
          <input
            className="input"
            type="password"
            id="password"
            name="password"
            placeholder="비밀번호"
            value={formData.password}
            onChange={handleChange}
            required
          />
        </div>
        <div className="input-group">
          <input
            className="input"
            type="email"
            id="email"
            name="email"
            placeholder="이메일"
            value={formData.email}
            onChange={handleChange}
            required
          />
        </div>
        <div className="input-group">
          <input
            className="input"
            type="text"
            id="name"
            name="name"
            placeholder="자녀 이름"
            value={formData.name}
            onChange={handleChange}
            required
          />
        </div>
        <button className="button" type="submit">
          회원가입
        </button>
      </form>
      <button className="secondary-button" onClick={() => navigate('/')}>
        로그인
      </button>
    </div>
  );
};

export default Signup;
