import axios from 'axios'

// In development VITE_API_URL is unset — requests use the Vite proxy (/api → :8000).
// In production set VITE_API_URL to the deployed backend base URL.
const http = axios.create({
  baseURL: import.meta.env.VITE_API_URL ?? '',
})

export interface Resource {
  title: string
  time: string
  type: string
  url: string
}

export interface Recommendation {
  skill: string
  resources: Resource[]
}

export interface FitAnalysis {
  matched_skills: string[]
  missing_skills: string[]
  extra_skills: string[]
  fit_percentage: number
  total_required: number
  total_matched: number
}

export interface AnalyzeResponse {
  domain: string
  fit_analysis: FitAnalysis
  recommendations: Recommendation[]
}

export interface AnalyzeRequest {
  cv_text: string
  job_text: string
  domain: string
}

export async function analyzeCV(request: AnalyzeRequest): Promise<AnalyzeResponse> {
  const { data } = await http.post<AnalyzeResponse>('/api/analyze', request)
  return data
}

export async function pingBackend(): Promise<void> {
  await http.get('/health', { timeout: 60_000 })
}
