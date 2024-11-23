import React from 'react';
import './ExamSelection.css';

const ExamSelection = ({ exams, selectExam }) => {
  return (
    <div className="exam-selection-container">
      {exams.map((exam) => (
        <button
          key={exam.id}
          onClick={() => selectExam(exam)}
          className="exam-button"
        >
          {exam.name}
        </button>
      ))}
    </div>
  );
};

export default ExamSelection;
