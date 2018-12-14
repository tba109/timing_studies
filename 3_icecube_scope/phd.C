void phd()
{
//=========Macro generated from canvas: c1/c1
//=========  (Tue May 22 18:12:43 2018) by ROOT version 6.12/06
   TCanvas *c1 = new TCanvas("c1", "c1",65,24,1855,1056);
   c1->ToggleEventStatus();
   c1->SetHighLightColor(2);
   c1->Range(-12.5,-18.76875,12.5,168.9188);
   c1->SetFillColor(0);
   c1->SetBorderMode(0);
   c1->SetBorderSize(2);
   c1->SetFrameBorderMode(0);
   c1->SetFrameBorderMode(0);
   
   TH1F *h1__1 = new TH1F("h1__1","",100,-10,10);
   h1__1->SetBinContent(6,1);
   h1__1->SetBinContent(12,1);
   h1__1->SetBinContent(22,1);
   h1__1->SetBinContent(24,1);
   h1__1->SetBinContent(25,1);
   h1__1->SetBinContent(28,2);
   h1__1->SetBinContent(29,2);
   h1__1->SetBinContent(30,6);
   h1__1->SetBinContent(31,11);
   h1__1->SetBinContent(32,13);
   h1__1->SetBinContent(33,26);
   h1__1->SetBinContent(34,31);
   h1__1->SetBinContent(35,46);
   h1__1->SetBinContent(36,62);
   h1__1->SetBinContent(37,70);
   h1__1->SetBinContent(38,63);
   h1__1->SetBinContent(39,89);
   h1__1->SetBinContent(40,46);
   h1__1->SetBinContent(41,53);
   h1__1->SetBinContent(42,43);
   h1__1->SetBinContent(43,25);
   h1__1->SetBinContent(44,30);
   h1__1->SetBinContent(45,40);
   h1__1->SetBinContent(46,35);
   h1__1->SetBinContent(47,25);
   h1__1->SetBinContent(48,22);
   h1__1->SetBinContent(49,143);
   h1__1->SetEntries(888);
   
   TPaveStats *ptstats = new TPaveStats(0.78,0.775,0.98,0.935,"brNDC");
   ptstats->SetName("stats");
   ptstats->SetBorderSize(1);
   ptstats->SetFillColor(0);
   ptstats->SetTextAlign(12);
   ptstats->SetTextFont(42);
   TText *ptstats_LaTex = ptstats->AddText("h1");
   ptstats_LaTex->SetTextSize(0.0368);
   ptstats_LaTex = ptstats->AddText("Entries = 888    ");
   ptstats_LaTex = ptstats->AddText("Mean  = -1.944");
   ptstats_LaTex = ptstats->AddText("Std Dev   =  1.125");
   ptstats->SetOptStat(1111);
   ptstats->SetOptFit(0);
   ptstats->Draw();
   h1__1->GetListOfFunctions()->Add(ptstats);
   ptstats->SetParent(h1__1);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   h1__1->SetLineColor(ci);
   h1__1->GetXaxis()->SetLabelFont(42);
   h1__1->GetXaxis()->SetLabelSize(0.035);
   h1__1->GetXaxis()->SetTitleSize(0.035);
   h1__1->GetXaxis()->SetTitleFont(42);
   h1__1->GetYaxis()->SetLabelFont(42);
   h1__1->GetYaxis()->SetLabelSize(0.035);
   h1__1->GetYaxis()->SetTitleSize(0.035);
   h1__1->GetYaxis()->SetTitleOffset(0);
   h1__1->GetYaxis()->SetTitleFont(42);
   h1__1->GetZaxis()->SetLabelFont(42);
   h1__1->GetZaxis()->SetLabelSize(0.035);
   h1__1->GetZaxis()->SetTitleSize(0.035);
   h1__1->GetZaxis()->SetTitleFont(42);
   h1__1->Draw("");
   c1->Modified();
   c1->cd();
   c1->SetSelected(c1);
}
