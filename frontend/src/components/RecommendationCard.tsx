import type { Recommendation } from '../services/api'

interface Props {
  recommendation: Recommendation
}

const TYPE_LABELS: Record<string, string> = {
  course: 'Course',
  video: 'Video',
  book: 'Book',
  article: 'Article',
  tutorial: 'Tutorial',
  practice: 'Practice',
  certificate: 'Certificate',
  reference: 'Reference',
}

export default function RecommendationCard({ recommendation }: Props) {
  return (
    <div className="rec-card">
      <h3 className="rec-skill">{recommendation.skill}</h3>
      <ul className="resource-list">
        {recommendation.resources.map((r, i) => (
          <li key={i} className="resource-item">
            <div className="resource-header">
              <a
                href={r.url}
                target="_blank"
                rel="noopener noreferrer"
                className="resource-title"
              >
                {r.title}
              </a>
              <span className={`type-badge type-${r.type}`}>
                {TYPE_LABELS[r.type] ?? r.type}
              </span>
            </div>
            <span className="resource-time">&#9201; {r.time}</span>
          </li>
        ))}
      </ul>
    </div>
  )
}
