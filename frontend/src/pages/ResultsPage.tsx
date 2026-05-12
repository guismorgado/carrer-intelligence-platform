import { useEffect } from 'react'
import { useLocation, useNavigate } from 'react-router-dom'
import FitBreakdown from '../components/FitBreakdown'
import RecommendationCard from '../components/RecommendationCard'
import type { AnalyzeResponse } from '../services/api'

const DOMAIN_LABELS: Record<string, string> = {
  management: 'Management',
  finance: 'Finance',
  business_analytics: 'Business Analytics',
}

export default function ResultsPage() {
  const location = useLocation()
  const navigate = useNavigate()
  const results = location.state?.results as AnalyzeResponse | undefined

  useEffect(() => {
    if (!results) navigate('/', { replace: true })
  }, [results, navigate])

  if (!results) return null

  const { domain, fit_analysis, recommendations } = results
  const hasMissing = fit_analysis.missing_skills.length > 0
  const hasRecommendations = recommendations.length > 0

  return (
    <div className="page">
      <div className="results-nav">
        <button className="btn-back" onClick={() => navigate('/')}>
          ← New Analysis
        </button>
        <span className="domain-badge">{DOMAIN_LABELS[domain] ?? domain}</span>
      </div>

      <h2 className="results-title">Your Fit Analysis</h2>

      <section className="card">
        <FitBreakdown analysis={fit_analysis} />
      </section>

      {hasRecommendations && (
        <section className="recommendations-section">
          <h2 className="section-title">Learning Recommendations</h2>
          <p className="section-subtitle">
            {recommendations.length} missing skill{recommendations.length !== 1 ? 's' : ''} with
            curated resources to close the gap.
          </p>
          <div className="rec-grid">
            {recommendations.map((rec) => (
              <RecommendationCard key={rec.skill} recommendation={rec} />
            ))}
          </div>
        </section>
      )}

      {!hasMissing && (
        <section className="card perfect-match">
          <p>&#127881; Perfect match — your CV covers all required skills for this role!</p>
        </section>
      )}

      {hasMissing && !hasRecommendations && (
        <section className="card">
          <p className="text-muted">
            Some skills are missing but we don't have curated resources for them yet.
            Check back soon as the resource library grows.
          </p>
        </section>
      )}
    </div>
  )
}
