import React, { useState } from "react";
import api from "../services/api";
import { useAuth } from "../context/AuthContext.jsx";

const ChallengeCard = ({ challenge }) => {
  const [answer, setAnswer] = useState("");
  const [feedback, setFeedback] = useState(null);
  const [error, setError] = useState(null);
  const { isAuthenticated } = useAuth();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setFeedback(null);
    setError(null);

    if (!isAuthenticated) {
      setError("You must be logged in to submit an answer.");
      return;
    }

    try {
      const response = await api.submitAnswer(challenge.id, answer);
      setFeedback(response.data.message);
    } catch (err) {
      if (err.response && err.response.data) {
        setError(err.response.data.detail || "Incorrect answer. Try again!");
      } else {
        setError("An unexpected error occurred. Please try again.");
      }
      console.error(err);
    }
  };

  return (
    <div className="challenge-card">
      <div className="flex justify-between items-start mb-4">
        <h3 className="text-xl font-bold text-slate-800 dark:text-slate-100">{challenge.title}</h3>
        <span className="bg-gradient-to-r from-purple-500 to-blue-500 text-white text-xs font-semibold px-3 py-1 rounded-full shadow-lg">
          {challenge.category}
        </span>
      </div>
      <p className="text-slate-600 dark:text-slate-300 mb-6 flex-grow leading-relaxed">{challenge.question}</p>
      
      <form onSubmit={handleSubmit} className="space-y-4">
        <input
          type="text"
          value={answer}
          onChange={(e) => setAnswer(e.target.value)}
          placeholder="Type your answer here"
          className="input-field"
          required
        />
        <button
          type="submit"
          className="btn-primary w-full"
        >
          Submit Answer
        </button>
      </form>

      {/* Feedback Section */}
      {feedback && (
        <div className="mt-4 p-4 text-center bg-gradient-to-r from-green-100 to-emerald-100 dark:from-green-900/30 dark:to-emerald-900/30 text-green-800 dark:text-green-300 rounded-xl border border-green-200 dark:border-green-700/30 backdrop-blur-sm">
          {feedback}
        </div>
      )}
      {error && (
        <div className="mt-4 p-4 text-center bg-gradient-to-r from-red-100 to-pink-100 dark:from-red-900/30 dark:to-pink-900/30 text-red-800 dark:text-red-300 rounded-xl border border-red-200 dark:border-red-700/30 backdrop-blur-sm">
          {error}
        </div>
      )}
    </div>
  );
};

export default ChallengeCard;

