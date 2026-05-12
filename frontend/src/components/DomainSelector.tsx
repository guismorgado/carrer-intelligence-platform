interface Props {
  value: string
  onChange: (value: string) => void
  disabled?: boolean
}

const DOMAINS = [
  { value: 'finance', label: 'Finance' },
  { value: 'management', label: 'Management' },
  { value: 'business_analytics', label: 'Business Analytics' },
]

export default function DomainSelector({ value, onChange, disabled }: Props) {
  return (
    <div className="field">
      <label className="label" htmlFor="domain">
        Domain
      </label>
      <select
        id="domain"
        className="select"
        value={value}
        onChange={(e) => onChange(e.target.value)}
        disabled={disabled}
      >
        {DOMAINS.map((d) => (
          <option key={d.value} value={d.value}>
            {d.label}
          </option>
        ))}
      </select>
    </div>
  )
}
