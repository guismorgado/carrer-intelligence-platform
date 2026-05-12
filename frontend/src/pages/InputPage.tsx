import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'
import DomainSelector from '../components/DomainSelector'
import { analyzeCV } from '../services/api'

const MIN_LENGTH = 100

export default function InputPage() {
  const navigate = useNavigate()
  const [cvText, setCvText] = useState('')
  const [jobText, setJobText] = useState('')
  const [domain, setDomain] = useState('finance')
  const [error, setError] = useState<string | null>(null)
  const [loading, setLoading] = useState(false)

  const cvReady = cvText.trim().length >= MIN_LENGTH
  const jobReady = jobText.trim().length >= MIN_LENGTH
  const canSubmit = cvReady && jobReady

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault()
    setError(null)
    setLoading(true)
    try {
      const results = await analyzeCV({ cv_text: cvText, job_text: jobText, domain })
      navigate('/results', { state: { results } })
    } catch (err) {
      if (axios.isAxiosError(err)) {
        const detail = err.response?.data?.detail
        setError(
          typeof detail === 'string'
            ? detail
            : 'Something went wrong. Is the backend running on port 8000?',
        )
      } else {
        setError('Unable to reach the server. Make sure the backend is running.')
      }
    } finally {
      setLoading(false)
    }
  }

  function charHint(text: string) {
    const remaining = MIN_LENGTH - text.trim().length
    if (remaining > 0) return { label: `${remaining} more characters needed`, ready: false }
    return { label: '✓ Ready', ready: true }
  }

  const cvHint = charHint(cvText)
  const jobHint = charHint(jobText)

  return (
    <div className="page">
      <header className="site-header">
        <h1 className="site-title">Career Intelligence Platform</h1>
        <p className="site-subtitle">
          Paste your CV and a job description to get a transparent fit analysis and personalised
          learning recommendations.
        </p>
      </header>

      <form className="input-card" onSubmit={handleSubmit} noValidate>
        <div className="text-areas">
          <div className="field">
            <label className="label" htmlFor="cv-text">
              Your CV
            </label>
            <textarea
              id="cv-text"
              className="textarea"
              placeholder="Paste the full text of your CV here..."
              rows={14}
              value={cvText}
              onChange={(e) => setCvText(e.target.value)}
              disabled={loading}
            />
            <span className={`char-hint ${cvHint.ready ? 'hint-ok' : 'hint-warn'}`}>
              {cvHint.label}
            </span>
          </div>

          <div className="field">
            <label className="label" htmlFor="job-text">
              Job Description
            </label>
            <textarea
              id="job-text"
              className="textarea"
              placeholder="Paste the full job description here..."
              rows={14}
              value={jobText}
              onChange={(e) => setJobText(e.target.value)}
              disabled={loading}
            />
            <span className={`char-hint ${jobHint.ready ? 'hint-ok' : 'hint-warn'}`}>
              {jobHint.label}
            </span>
          </div>
        </div>

        <div className="form-footer">
          <DomainSelector value={domain} onChange={setDomain} disabled={loading} />
          <button className="btn-analyze" type="submit" disabled={!canSubmit || loading}>
            {loading ? 'Analysing…' : 'Analyse My Fit'}
          </button>
        </div>

        {error && <p className="error-msg">{error}</p>}
      </form>
    </div>
  )
}
