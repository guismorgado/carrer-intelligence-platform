import type { FitAnalysis } from '../services/api'

interface Props {
  analysis: FitAnalysis
}

function FitCircle({ percentage }: { percentage: number }) {
  const radius = 54
  const circumference = 2 * Math.PI * radius
  const offset = circumference - (Math.min(percentage, 100) / 100) * circumference
  const color =
    percentage >= 70 ? 'var(--matched)' : percentage >= 40 ? 'var(--extra)' : 'var(--missing)'

  return (
    <svg width="140" height="140" viewBox="0 0 140 140" aria-label={`${percentage}% fit score`}>
      <circle cx="70" cy="70" r={radius} fill="none" stroke="var(--border)" strokeWidth="12" />
      <circle
        cx="70"
        cy="70"
        r={radius}
        fill="none"
        stroke={color}
        strokeWidth="12"
        strokeLinecap="round"
        strokeDasharray={circumference}
        strokeDashoffset={offset}
        transform="rotate(-90 70 70)"
      />
      <text
        x="70" y="64"
        textAnchor="middle"
        dominantBaseline="central"
        fontSize="26"
        fontWeight="700"
        fill={color}
        fontFamily="inherit"
      >
        {percentage}%
      </text>
      <text x="70" y="88" textAnchor="middle" fontSize="11" fill="var(--text-muted)" fontFamily="inherit">
        fit score
      </text>
    </svg>
  )
}

export default function FitBreakdown({ analysis }: Props) {
  const { matched_skills, missing_skills, extra_skills, fit_percentage, total_required, total_matched } =
    analysis

  return (
    <div className="fit-breakdown">
      <div className="fit-score-section">
        <FitCircle percentage={fit_percentage} />
        <div>
          <p className="fit-summary-main">
            {total_matched} of {total_required} required skills matched
          </p>
          <p className="fit-summary-sub">
            {missing_skills.length > 0
              ? `${missing_skills.length} skill${missing_skills.length !== 1 ? 's' : ''} to develop`
              : 'All required skills covered'}
          </p>
        </div>
      </div>

      <div className="skill-columns">
        <div className="skill-col">
          <h3 className="skill-col-header matched-header">
            &#10003; Matched <span className="count">{matched_skills.length}</span>
          </h3>
          <div className="skill-tags">
            {matched_skills.length > 0
              ? matched_skills.map((s) => (
                  <span key={s} className="skill-tag matched-tag">{s}</span>
                ))
              : <span className="no-skills">None found</span>}
          </div>
        </div>

        <div className="skill-col">
          <h3 className="skill-col-header missing-header">
            &#10007; Missing <span className="count">{missing_skills.length}</span>
          </h3>
          <div className="skill-tags">
            {missing_skills.length > 0
              ? missing_skills.map((s) => (
                  <span key={s} className="skill-tag missing-tag">{s}</span>
                ))
              : <span className="no-skills">None — perfect match!</span>}
          </div>
        </div>

        <div className="skill-col">
          <h3 className="skill-col-header extra-header">
            + Extra <span className="count">{extra_skills.length}</span>
          </h3>
          <div className="skill-tags">
            {extra_skills.length > 0
              ? extra_skills.map((s) => (
                  <span key={s} className="skill-tag extra-tag">{s}</span>
                ))
              : <span className="no-skills">None</span>}
          </div>
        </div>
      </div>
    </div>
  )
}
