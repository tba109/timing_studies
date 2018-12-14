void 1000MSPS()
{
//=========Macro generated from canvas: c1/c1
//=========  (Mon May 21 20:48:24 2018) by ROOT version 6.12/06
   TCanvas *c1 = new TCanvas("c1", "c1",65,52,700,500);
   c1->SetHighLightColor(2);
   c1->Range(-50,-5.64375,50,50.79375);
   c1->SetFillColor(0);
   c1->SetBorderMode(0);
   c1->SetBorderSize(2);
   c1->SetFrameBorderMode(0);
   c1->SetFrameBorderMode(0);
   
   TH1F *h1__1 = new TH1F("h1__1","",400,-40,40);
   h1__1->SetBinContent(256,1);
   h1__1->SetBinContent(257,1);
   h1__1->SetBinContent(258,7);
   h1__1->SetBinContent(259,11);
   h1__1->SetBinContent(260,28);
   h1__1->SetBinContent(261,25);
   h1__1->SetBinContent(262,24);
   h1__1->SetBinContent(263,30);
   h1__1->SetBinContent(264,42);
   h1__1->SetBinContent(265,35);
   h1__1->SetBinContent(266,41);
   h1__1->SetBinContent(267,43);
   h1__1->SetBinContent(268,32);
   h1__1->SetBinContent(269,32);
   h1__1->SetBinContent(270,24);
   h1__1->SetBinContent(271,17);
   h1__1->SetBinContent(272,10);
   h1__1->SetBinContent(273,11);
   h1__1->SetBinContent(274,11);
   h1__1->SetBinContent(275,8);
   h1__1->SetBinContent(276,6);
   h1__1->SetBinContent(277,9);
   h1__1->SetBinContent(278,7);
   h1__1->SetBinContent(279,3);
   h1__1->SetBinContent(280,2);
   h1__1->SetBinContent(281,2);
   h1__1->SetBinContent(282,1);
   h1__1->SetBinContent(283,1);
   h1__1->SetBinContent(284,2);
   h1__1->SetBinContent(285,3);
   h1__1->SetBinContent(286,1);
   h1__1->SetBinContent(287,1);
   h1__1->SetBinContent(289,1);
   h1__1->SetBinContent(292,2);
   h1__1->SetBinContent(295,1);
   h1__1->SetBinContent(299,1);
   h1__1->SetEntries(476);
   
   TF1 *f11 = new TF1("f1","gaus",-40,40, TF1::EAddToList::kNo);
   f11->SetFillColor(19);
   f11->SetFillStyle(0);
   f11->SetLineColor(2);
   f11->SetLineWidth(2);
   f11->SetChisquare(60.65617);
   f11->SetNDF(33);
   f11->GetXaxis()->SetLabelFont(42);
   f11->GetXaxis()->SetLabelSize(0.035);
   f11->GetXaxis()->SetTitleSize(0.035);
   f11->GetXaxis()->SetTitleFont(42);
   f11->GetYaxis()->SetLabelFont(42);
   f11->GetYaxis()->SetLabelSize(0.035);
   f11->GetYaxis()->SetTitleSize(0.035);
   f11->GetYaxis()->SetTitleOffset(0);
   f11->GetYaxis()->SetTitleFont(42);
   f11->SetParameter(0,39.7961);
   f11->SetParError(0,2.659234);
   f11->SetParLimits(0,0,0);
   f11->SetParameter(1,13.14387);
   f11->SetParError(1,0.04925374);
   f11->SetParLimits(1,0,0);
   f11->SetParameter(2,0.8370243);
   f11->SetParError(2,0.03904727);
   f11->SetParLimits(2,0,12.11167);
   f11->SetParent(h1__1);
   h1__1->GetListOfFunctions()->Add(f11);
   
   TPaveStats *ptstats = new TPaveStats(0.78,0.775,0.98,0.935,"brNDC");
   ptstats->SetName("stats");
   ptstats->SetBorderSize(1);
   ptstats->SetFillColor(0);
   ptstats->SetTextAlign(12);
   ptstats->SetTextFont(42);
   TText *ptstats_LaTex = ptstats->AddText("h1");
   ptstats_LaTex->SetTextSize(0.0368);
   ptstats_LaTex = ptstats->AddText("Entries = 476    ");
   ptstats_LaTex = ptstats->AddText("Mean  =  13.34");
   ptstats_LaTex = ptstats->AddText("Std Dev   =  1.214");
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
